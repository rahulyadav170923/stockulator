function Est = brownian(S0)
filename = 'D:\hackathon\table2.xlsx';
format bank
sheet=1;
xlRange = 'B2:B210';
x2Range = 'E2:E210';

seta = xlsread(filename,sheet,xlRange);
setb = xlsread(filename,sheet,x2Range);
 
format long
n = ones(size(seta));
for i =1:length(seta)-1
    n(i) = (log((seta(i+1)/seta(i))));
end;
avg = mean(n(1:(size(n)-1)));
variance = var(n(1:(size(n)-1)));
 
delt=1/(length(n)-1);
volatility_sigma = sqrt(variance/delt);
drift_mu = ((avg + (variance/2))/delt);
Est=S0*exp(drift_mu*delt)
end


