%define _build_id_links none

# global info
%global repo 23.20.00.48
%global major 23.20.00.48
%global minor 1666589
# pkg info
%global amf 1.4.31
%global enc 1.0
%global amdvlk 2023.Q3.3
# drm info
%global drm 2.4.115.50700-1666569
%global amdgpu 1.0.0.50700-1666569
# firmware info
%global firmware_rev 6.2.4
%global firmware_maj 50700
%global firmware_min 1666569
%global _firmwarepath	/usr/lib/firmware
# Distro info
%global fedora 39
%global ubuntu 22.04

Name:     amd-gpu-pro-firmware
Version:  %{repo}
Release:  1%{?dist}
License:       AMDGPU PRO  EULA NON-REDISTRIBUTABLE
Group:         System Environment/Libraries
Summary:       System runtime for AMD Advanced Media Framework
URL:      http://repo.radeon.com/amdgpu

%undefine _disable_source_fetch
Source0:  http://repo.radeon.com/amdgpu/%{repo}/ubuntu/pool/main/a/amdgpu-dkms/amdgpu-dkms-firmware_%{firmware_rev}.%{firmware_maj}-%{firmware_min}.%{ubuntu}_all.deb

Provides:      amd-gpu-firmware
Obsoletes:	amd-gpu-firmware

BuildRequires: wget 
BuildRequires: cpio

Requires(post): /usr/bin/dracut 
Requires(postun): /usr/bin/dracut

%description
Firmware required for AMD AMF encoder support

%prep
mkdir -p files

ar x --output . %{SOURCE0}
tar -xJC files -f data.tar.xz || tar -xC files -f data.tar.gz

%install
mkdir -p %{buildroot}/usr/lib/firmware/amdgpu
cp -r files/usr/src/amdgpu-%{firmware_rev}-%{firmware_min}.%{ubuntu}/firmware/amdgpu/* %{buildroot}%{_firmwarepath}/amdgpu/ || true
cp -r files/lib/firmware/updates/amdgpu/* %{buildroot}%{_firmwarepath}/amdgpu/

%files
%{_firmwarepath}/amdgpu/

%post
/usr/bin/dracut -f

%postun
/usr/bin/dracut -f
