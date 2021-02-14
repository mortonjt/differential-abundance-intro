data {
  int<lower=0> N;    // number of samples
  int<lower=0> p;    // number of covariates
  real depth[N];     // sequencing depths of microbes
  matrix[N, p] x;    // covariate matrix
  int y[N];          // observed microbe abundances
}

parameters {
  // parameters required for linear regression on the species means
  vector[p] beta;                 // covariates
  real<lower=0> disp;
}

transformed parameters {
  vector[N] lam;
  vector[N] lam_clr;
  vector[N] z;

  z = to_vector(rep_array(0, N));
  lam = x * beta;
  lam_clr = append_col(z, lam);
}

model {
  // setting priors ...
  disp ~ inv_gamma(1., 1.);
  beta ~ normal(0., 10.); // uninformed prior
  // generating counts
  for (n in 1:N){
    target += neg_binomial_2_log_lpmf(y[n] | depth[n] + lam[n], disp);
  }
}
