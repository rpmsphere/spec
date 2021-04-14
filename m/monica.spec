%undefine _debugsource_packages

Name:           monica
Version:        3.7
Release:        21.1
License:        BSD-3-Clause
Summary:        Monitor Calibration Tool
URL:            http://www.pcbypaul.com/software/monica.html
Group:          System/X11/Utilities
Source0:        %{name}-%{version}.tar.bz2
Source1:        %{name}.desktop
Source2:        %{name}.png
# PATCH-FIX-UPSTREAM monica-3.7-gcc44.patch lazy.kent@opensuse.org -- fix build with gcc 4.4
Patch0:         monica-3.7-gcc44.patch
# PATCH-FIX-UPSTREAM monica-3.7-makefile.patch lazy.kent@opensuse.org -- fix optflags
Patch1:         monica-3.7-makefile.patch
BuildRequires:  fltk-devel
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xft)
BuildRequires:  pkgconfig(xinerama)

%description
Monica is a small monitor calibration tool.
It works as frontend to xgamma which uses the FLTK library
(www.fltk.org). With Monica you can alter your monitor's gamma on
XFree86 or Xorg. The gray and color scales can help you find usable
settings. The grey box with lines illustrates a display gamma of 2.2,
the sRGB standard gamma.

%prep
%setup -q
%patch0
%patch1

%build
make %{?_smp_mflags}

%install
install -Dm 0755 %{name} $RPM_BUILD_ROOT%{_bindir}/%{name}
install -Dm 0644 %{SOURCE1} \
    $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop
install -Dm 0644 %{SOURCE2} \
    $RPM_BUILD_ROOT%{_datadir}/pixmaps/%{name}.png

%files
%doc authors ChangeLog licence news readme
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png

%changelog
* Wed Aug 01 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 3.7
- Rebuilt for Fedora
* Sun Apr 29 2012 lazy.kent@opensuse.org
-  Use pkgconfig(*) as build dependencies.
* Sun Jul 24 2011 lazy.kent@opensuse.org
- Build requires xorg-x11-devel.
- Corrected makefile patch.
- Minor spec formatting.
* Sun Nov 15 2009 lazy.kent.suse@gmail.com
- Makefile patch to fix optflags.
* Thu Oct 15 2009 lazy.kent.suse@gmail.com
- Corrected License and Summary.
* Sun Jun 14 2009 lazy.kent.suse@gmail.com
- GCC 4.4 patch.
* Wed Mar 18 2009 lazy.kent.suse@gmail.com
- Initial package created 3.7.
