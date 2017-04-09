import scipy.io.wavfile
import bob.ap
import numpy

rate, signal = scipy.io.wavfile.read(str('7100300N.wav')) 
print rate
print signal
print len(signal)/rate

win_length_ms = 20 # The window length of the cepstral analysis in milliseconds
win_shift_ms = 10 # The window shift of the cepstral analysis in milliseconds
n_filters = 24 # The number of filter bands
n_ceps = 19 # The number of cepstral coefficients
f_min = 0. # The minimal frequency of the filter bank
f_max = 4000. # The maximal frequency of the filter bank
delta_win = 2 # The integer delta value used for computing the first and second order derivatives
pre_emphasis_coef = 0.97 # The coefficient used for the pre-emphasis
dct_norm = True # A factor by which the cepstral coefficients are multiplied
mel_scale = True # Tell whether cepstral features are extracted on a linear (LFCC) or Mel (MFCC) scale

c = bob.ap.Ceps(rate, win_length_ms, win_shift_ms, n_filters, n_ceps, f_min, f_max, delta_win, pre_emphasis_coef, mel_scale, dct_norm)
signal = numpy.cast['float'](signal) # vector should be in **float**
mfcc = c(signal)
print len(mfcc)
print len(mfcc[0])
print 'mfcc',mfcc
c.mel_scale = False
lfcc = c(signal)
c.with_energy = True
lfcc_e = c(signal)
print len(lfcc_e)
print len(lfcc_e[0])
c.with_delta = True
c.with_delta_delta = True
lfcc_e_d_dd = c(signal)
print len(lfcc_e_d_dd)
print len(lfcc_e_d_dd[0])


