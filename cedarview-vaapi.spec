Summary: Intel® Linux PowerVR !Graphics/Media vaapi Drivers for CedarTrail
Name:    cedarview-vaapi
Version: 1.0.1
Release: 1%{dist}.bin
Group:   Development/Libraries       
License: Proprietary
#Source: http://downloadmirror.intel.com/21519/eng/cdv-gfx-drivers-1.0.1_bee.tar.bz2
Source: cedarview-vaapi-v1.0.1_bee.tar.bz2
BuildRoot: %{_tmppath}%{name}-%{version}-build
URL: http://downloadcenter.intel.com/Detail_Desc.aspx?agr=Y&DwnldID=21519
ExclusiveArch: %ix86
   
%description
Unpack the PVR VA-API driver for Cedartrail-accelerated H.264, MPEG-2, and
VC1 streams.

%prep
%setup -q -c

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT
cp -a * $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(-,root,root,-)
/lib/firmware/*
%exclude /license.txt
/usr/lib/dri/*

%changelog
* Wed Jul 25 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 1.0.1
- Initial package for OSSII
