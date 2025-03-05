#include <kfr/base.hpp>
#include <kfr/dsp.hpp>
#include <kfr/io.hpp>

using namespace kfr;

int main()
{
    // Print the version of the KFR library being used
    println(library_version());

    // Define an output univector with 1024 elements
    univector<fbase, 1024> output;

    // --------------------------------------------------------------------------------------
    // ------------------------ 24th-Order Butterworth Lowpass Filter -----------------------
    // --------------------------------------------------------------------------------------
    {
        // Create a 24th-order Butterworth lowpass filter with a cutoff frequency of 1 kHz and a sample rate
        // of 48 kHz
        zpk<fbase> filt = iir_lowpass(butterworth<fbase>(24), 1000, 48000);

        // Apply the filter to a unit impulse signal to get the filter's impulse response
        output = iir(unitimpulse(), filt);
    }
    println("24th-order Butterworth lowpass filter applied");

    // Print first 10 values of the output
    println("First 10 values of the output:");
    for (size_t i = 0; i < 10; ++i)
        println(output[i]);

    // --------------------------------------------------------------------------------------
    // ------------------------ 12th-Order Butterworth Lowpass Filter -----------------------
    // --------------------------------------------------------------------------------------
    {
        // Create a 12th-order Butterworth lowpass filter with a cutoff frequency of 1 kHz and a sample rate
        // of 48 kHz
        zpk<fbase> filt = iir_lowpass(butterworth<fbase>(12), 1000, 48000);

        // Apply the filter to a unit impulse signal to get the filter's impulse response
        output = iir(unitimpulse(), filt);
    }
    println("12th-order Butterworth lowpass filter applied");

    // Print first 10 values of the output
    println("First 10 values of the output:");
    for (size_t i = 0; i < 10; ++i)
        println(output[i]);

    // --------------------------------------------------------------------------------------
    // ------------------------ 12th-Order Butterworth Highpass Filter ----------------------
    // --------------------------------------------------------------------------------------
    {
        // Create a 12th-order Butterworth highpass filter with a cutoff frequency of 1 kHz and a sample rate
        // of 48 kHz
        zpk<fbase> filt = iir_highpass(butterworth<fbase>(12), 1000, 48000);

        // Convert the filter to second-order sections (SOS).
        // This is an expensive operation, so keep 'iir_params' if it is reused later
        iir_params<fbase> bqs = to_sos(filt);

        // Apply the filter to a unit impulse signal to get the filter's impulse response
        output = iir(unitimpulse(), bqs);
    }
    println("12th-order Butterworth highpass filter applied");

    // Print first 10 values of the output
    println("First 10 values of the output:");
    for (size_t i = 0; i < 10; ++i)
        println(output[i]);

    // --------------------------------------------------------------------------------------
    // ---------------------- 12th-Order Butterworth Bandpass Filter ------------------------
    // --------------------------------------------------------------------------------------
    {
        // Create a 12th-order Butterworth bandpass filter with a passband from 0.1 to 0.2 (normalized
        // frequency)
        zpk<fbase> filt = iir_bandpass(butterworth<fbase>(12), 0.1, 0.2);

        // Convert the filter to second-order sections (SOS).
        // This is an expensive operation, so keep 'iir_params' if it is reused later
        iir_params<fbase> bqs = to_sos(filt);

        // Apply the filter to a unit impulse signal to get the filter's impulse response
        output = iir(unitimpulse(), bqs);
    }
    println("12th-order Butterworth bandpass filter applied");

    // Print first 10 values of the output
    println("First 10 values of the output:");
    for (size_t i = 0; i < 10; ++i)
        println(output[i]);

    // --------------------------------------------------------------------------------------
    // ---------------------- 12th-Order Butterworth Bandstop Filter ------------------------
    // --------------------------------------------------------------------------------------
    {
        // Create a 12th-order Butterworth bandstop filter with a stopband from 0.1 to 0.2 (normalized
        // frequency)
        zpk<fbase> filt = iir_bandstop(butterworth<fbase>(12), 0.1, 0.2);

        // Convert the filter to second-order sections (SOS).
        // This is an expensive operation, so keep 'iir_params' if it is reused later
        iir_params<fbase> bqs = to_sos(filt);

        // Apply the filter to a unit impulse signal to get the filter's impulse response
        output = iir(unitimpulse(), bqs);
    }
    println("12th-order Butterworth bandstop filter applied");

    // Print first 10 values of the output
    println("First 10 values of the output:");
    for (size_t i = 0; i < 10; ++i)
        println(output[i]);

    // --------------------------------------------------------------------------------------
    // ------------------------ 4th-Order Butterworth Bandpass Filter -----------------------
    // --------------------------------------------------------------------------------------
    {
        // Create a 4th-order Butterworth bandpass filter with a passband from 0.005 to 0.9 (normalized
        // frequency)
        zpk<fbase> filt = iir_bandpass(butterworth<fbase>(4), 0.005, 0.9);

        // Convert the filter to second-order sections (SOS).
        // This is an expensive operation, so keep 'iir_params' if it is reused later
        iir_params<fbase> bqs = to_sos(filt);

        // Apply the filter to a unit impulse signal to get the filter's impulse response
        output = iir(unitimpulse(), bqs);
    }
    println("4th-order Butterworth bandpass filter applied");

    // Print first 10 values of the output
    println("First 10 values of the output:");
    for (size_t i = 0; i < 10; ++i)
        println(output[i]);

    println("Filter applications completed successfully");

    return 0;
}
