data {
  int<lower=0> N;     // number of samples
  int<lower=0> D;     // number of samples
  int<lower=0> p;     // number of covariates
  real depth[N];      // sequencing depths of microbes
  matrix[N, p] x;     // covariate matrix
  int y[N, D];        // observed microbe abundances
}

parameters {
  // parameters required for linear regression on the species means
  matrix[p, D-1] beta;  // covariates
  real<lower=0> disp; // over-dispersion to help control for variance
}

transformed parameters {
  matrix[N, D] lam;
  vector[N] z;

  z = to_vector(rep_array(0, N));
  lam = append_col(z, x * beta);
}

model {
  // setting priors ...
  disp ~ inv_gamma(1., 1.);
  to_vector(beta) ~ normal(0., 10.); // uninformed prior
  // generating counts
  for (n in 1:N){
    for (d in 1:D){
      target += neg_binomial_2_log_lpmf(y[n, d] | depth[n] + lam[n, d], disp);
    }
  }
}
