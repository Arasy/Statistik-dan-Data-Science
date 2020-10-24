library(tidyverse)
library(dplyr)
setwd("C:/Users/Arasy/Documents/Dosen/Kuliah 20201/R kursus")

#buka file dengan kolom tertentu
data = read.csv("karyawan.csv") %>% select( "ID", "Nama.Pegawai", "Tanggal.Lahir", "Berat",  "Tinggi")

#fungsi dan apply ke kolom barunya, alt 1,2,3
panjang <- function(a){
  return(nchar(a))
}

data$panjang = panjang(data$Nama.Pegawai)
data$panjang2 = sapply(data$Nama.Pegawai, panjang)
data = data %>% mutate(panjang3 = panjang(data$Nama.Pegawai))

# split by tahun dan bulan
data <- separate(data,"Tanggal.Lahir",c("tgl","bulan","tahun"),sep="-")
data$tgl = as.numeric(data$tgl)
data$bulan = as.numeric(data$bulan)

#pilih satu dari group
resume <- data %>% group_by(bulan)%>% filter(Berat == max(Berat)) %>% filter(Tinggi == max(Tinggi)) %>% filter(tgl == min(tgl)) %>% ungroup()
rcount <- data %>% count(bulan)
rsum <- data %>% group_by(bulan) %>% summarise(totalberat = sum(Berat), totaltinggi = sum(Tinggi)) %>% ungroup()

#merging hasil
resume = merge(resume,rcount,by='bulan')
resume = merge(resume,rsum, by='bulan')



#select na
#data baca dari datana.txt
datana <- data[is.na(data$QnSize),][c("ID","QnSinV1","QnSinV2","QnSinV3","QnSize","QnWt")]

#save ke spreadsheet
write.csv(datana,"datana.csv")
