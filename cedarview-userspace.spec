Summary: Intel® Linux PowerVR !Graphics/Media userspace Drivers for CedarTrail
Name:    cedarview-userspace
Version: 1.0.1
Release: 1%{dist}.bin
Group:   Development/Libraries       
License: Proprietary
#Source: http://downloadmirror.intel.com/21519/eng/cdv-gfx-drivers-1.0.1_bee.tar.bz2
Source: cedarview-userspace-v1.0.1_bee.tar.bz2
BuildRoot: %{_tmppath}%{name}-%{version}-build
URL: http://downloadcenter.intel.com/Detail_Desc.aspx?agr=Y&DwnldID=21519
ExclusiveArch: %ix86
   
%description
Unpack and install the appropriate userspace (Xorg, 2D, 3D) Cedarview drivers
relative to your root filesystem. While the PowerVR driver is a Mesa
replacement for EGL and GL ES, mesa-libGL of the stated version is required for
OpenGL operation. Note that development headers are installed as well.

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
/usr/lib/dri/pvr_dri.so
/usr/lib/lib*
/usr/lib/pkgconfig/*
/usr/lib/xorg/modules/drivers/pvr_drv.so
%{_datadir}/doc/powervr/license.txt
%{_includedir}/*
%{_sysconfdir}/X11/xorg.conf.d/cdv-pvr.conf
%{_sysconfdir}/powervr.ini
%{_sysconfdir}/pvr-version.txt

%changelog
* Wed Jul 25 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 1.0.1
- Initial package for OSSII
