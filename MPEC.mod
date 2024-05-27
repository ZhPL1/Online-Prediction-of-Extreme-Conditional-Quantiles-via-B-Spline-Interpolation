param tau;
set OBS;
param X {j in OBS};
param Y {j in OBS};
param X0;

var alpha;
var beta;
var gamma >= 0.00001;
var sigma >= 0.00001;
var lam_pos {OBS};
var lam_neg {OBS};
var u {OBS};
var t_pos {OBS};
var t_neg {OBS};
var Z {j in OBS} = Y[j] - alpha - beta*X0;
var I {j in OBS} = (if Z[j] >= 0 then 1 else 0);
var T {j in OBS} = max(0, Z[j]);
var O {j in OBS} = (if gamma = 0 then T[j]/sigma else (1+gamma)/gamma * log(1+gamma*T[j]/sigma));

minimize OBJ:
	sum {j in OBS}
		 (O[j] + log(sigma))*I[j];

subject to YX {j in OBS}:
	Y[j] = alpha + beta*X[j] + lam_pos[j] - lam_neg[j];
subject to TUP {j in OBS}:
	tau - u[j] - t_pos[j] = 0;
subject to TUN {j in OBS}:
	1 - tau + u[j] - t_neg[j] = 0;	
subject to LTP {j in OBS}:
	lam_pos[j] * t_pos[j] = 0;
subject to LTN {j in OBS}:
	lam_neg[j] * t_neg[j] = 0;	
subject to LP {j in OBS}:
	lam_pos[j] >= 0;
subject to LN {j in OBS}:
	lam_neg[j] >= 0;
subject to TP {j in OBS}:
	t_pos[j] >= 0;
subject to TN {j in OBS}:
	t_neg[j] >= 0;
subject to SUMU:
	sum {j in OBS} u[j] = 0;
subject to SUMUX:
	sum {j in OBS} u[j]*X[j] = 0;
	

	

