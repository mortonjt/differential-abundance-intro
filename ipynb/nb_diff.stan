data {
  int<lower=0> n;     // number of samples
  int<lower=0> d;     // number of samples
  int<lower=0> p;     // number of covariates
  real depth[n];      // sequencing depths of microbes (in log counts)
  matrix[n, p] x;     // covariate matrix
  int y[n, d];        // observed microbe abundances
}

parameters {
  // parameters required for linear regression on the species means
  matrix[p, d-1] beta;  // covariates
  real<lower=0> disp; // over-dispersion to help control for variance
}

transformed parameters {
  matrix[n, d] lam;
  // compute log(alr^{-1}(x * \beta))
  lam = append_col(to_vector(rep_array(0, n)), x * beta);
}

model {
  // setting priors ...
  disp ~ inv_gamma(1., 1.);
  to_vector(beta) ~ normal(0., 10.); // uninformed prior
  // generating counts
  for (i in 1:n){
    for (j in 1:d){
      target += neg_binomial_2_log_lpmf(y[i, j] | depth[n] + lam[i, j], disp);
    }
  }
}
