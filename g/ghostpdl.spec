Summary:        Ghostscript RIP for PCL-5, PCL-XL and XPS
Name:           ghostpdl
Version:        10.01.2
Release:        1
URL:            https://github.com/ArtifexSoftware/ghostpdl
License:        GPL
Group:          Applications/Forensics Tools
Source:         https://github.com/ArtifexSoftware/ghostpdl/archive/refs/tags/%{name}-%{version}.tar.xz
BuildRequires:  libXt-devel libXext-devel
BuildRequires:  libtool
BuildRequires:  autoconf

%description
GhostPDL is Artifex Software's implementation of the PCL-5™ and PCL-XL™ family
of page description languages.

%prep
%setup -q

%build
./autogen.sh
#rm -f ijs/ltmain.sh 
#ln -s /usr/share/libtool/build-aux/ltmain.sh ijs/ltmain.sh
%configure
%make_build

%install
#make_install
install -Dp -m755 bin/gpcl6 %{buildroot}%{_bindir}/pcl6
install -Dp -m755 bin/gxps %{buildroot}%{_bindir}/xps
install -Dp -m644 doc/pclxps/ghostpdl.pdf %{buildroot}%{_docdir}/%{name}/%{name}.pdf

%post
if [ -f /opt/xplico/bin/pcl6 ]; then
        echo "Updating xplico installation with new ghostpdl binary (pcl6)"
        cp -p /usr/bin/pcl6 /opt/xplico/bin/pcl6 
fi

%files
%doc doc/*
%{_bindir}/*
%{_docdir}/%{name}/%{name}.pdf

%changelog
* Sun Sep 17 2023 Wei-Lun Chao <bluebat@member.fsf.org> - 10.01.2
- Rebuilt for Fedora
* Fri Oct  4 2019 Lawrence R. Rogers <lrr@cert.org> 9.27-1
* Release 9.27-1
        Version 9.27
* Fri Aug  4 2017 Lawrence R. Rogers <lrr@cert.org> 9.21-1
* Release 9.21-1
        Version 9.21
* Fri Dec 18 2015 Lawrence R. Rogers <lrr@cert.org> 9.18-1
* Release 9.18-1
        Version 9.18
* Mon Sep 22 2014 Lawrence R. Rogers <lrr@cert.org> 9.15-1
* Release 9.15-1
        Version 9.15
* Mon Sep 02 2013 Lawrence R. Rogers <lrr@cert.org> 9.10-1
* Release 9.10-1
        Version 9.10
* Mon Aug 26 2013 Lawrence R. Rogers <lrr@cert.org> 9.09-1
* Release 9.09-1
        Version 9.09
* Thu Aug 15 2013 Lawrence R. Rogers <lrr@cert.org> 9.08-1
* Release 9.08-1
        Version 9.08
* Thu Feb 14 2013 Lawrence R. Rogers <lrr@cert.org> 9.07-1
* Release 9.07-1
        Version 9.07
* Wed Aug 8 2012 Lawrence R. Rogers <lrr@cert.org> 9.06-1
* Release 9.06-1
        Version 9.06
* Wed Feb 8 2012 Lawrence R. Rogers <lrr@cert.org> 9.05-1
* Release 9.05-1
        Version 9.05
* Mon Aug 1 2011 Lawrence R. Rogers <lrr@cert.org> 9.04-1
* Release 9.04-1
        * This release is primarily a bug fixing release with some
          improvements to auto configuration for unix and Mac OS X
          environments.
* Tue Mar 1 2011 Lawrence R. Rogers <lrr@cert.org> 9.02-1
* Release 9.02-1
        * Revised approach for applying a halftone to sampled image data
          for monochrome output devices.
* Tue Feb 1 2011 Lawrence R. Rogers <lrr@cert.org> 9.01-1
* Release 9.01-1
        * Adds this file (NEWS) to document newsworthy changes since the last
          release.
        * Profile configurations for Visual Studio projects are now supported.
        * Implementation for JPEG-XR (previously known as HD-Photo) has been
          completed for XPS.
        * The languages: PCL, XPS and SVG, now support and default to the
          display device on Windows.
        * Optimizations related to clipping and blank pages, for details see
          logs for revisions 12036 and 12027.
        * pcl/PCL5C_Color_Laserjet_4700_Differences.xls and
          pxl/PXL_Color_Laserjet_4700_Differences.xls document and illustrate
          differences between the Artifex PCL interpreter and the HP Color
          Laserjet 4700.
        * Include the new tiffscaled device.  This entry overlaps with a
          similar news entry in ghostscript news but the device is important
          for PCL fax customers and was worthy of mention here as well.  See
          Ghostscript news for details.
        * The languages (PCL, XPS and SVG) now support the ps2write device.
          This is intended to replace pswrite which will eventually be
          deprecated in a future release.  The output of ps2write is
          DSC-compliant level 2 PostScript.
