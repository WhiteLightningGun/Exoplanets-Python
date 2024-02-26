import lightkurve as lk
import matplotlib.pyplot as plt

TIC = 'TIC 410214986'  # Binary star system DS Tucanae

# grab TESS experiment data from open source database
sector_data = lk.search_lightcurve(
    TIC, mission='TESS', author='SPOC', sector=28).download_all()

# Extract time and flux values from first array in TargetPixelFileCollection returned from lk
time = sector_data[0].time.value
flux = sector_data[0].flux.value

# Determine the number of complete chunks of 100 we can get from our data
num_chunks = len(time) // 100

# Reshape the time and flux arrays to have 100 elements per row
time_reshaped = time[:num_chunks*100].reshape(-1, 100)
flux_reshaped = flux[:num_chunks*100].reshape(-1, 100)

# Calculate the mean time and flux for each chunk
mean_time = time_reshaped.mean(axis=1)
mean_flux = flux_reshaped.mean(axis=1)

# Create a new figure
plt.figure()

# Plot time vs flux
# n.b. time is in units of days relative to the TESS mission, flux is in electrons per second
# plot as scatter plot with small blue dots
plt.scatter(time, flux, color='blue', label='Flux', s=1)

# Plot the average flux per 100 units of time
plt.plot(mean_time, mean_flux, color='orange',
         label='Average flux per 100 time units')

# Set the title and labels
plt.title('TESS: DS Tucanae Time vs Flux')
plt.xlabel('Time (days)')
plt.ylabel('Flux (e-/s)')

# Add a legend
plt.legend()

plt.show()
