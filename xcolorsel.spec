%global debug_package %{nil}

Summary: Simple color displayer/selector for X11 rgb.txt files
Name: xcolorsel
Version: 1.1a
Release: 32.1
BuildRequires: libX11-devel libXt-devel libXext-devel
BuildRequires: libXpm-devel libXmu-devel libXp-devel
BuildRequires: libXau-devel Xaw3d-devel xorg-x11-utils
BuildRequires: imake
%define docdir %{_docdir}/%{name}-%{version}
Source0: %{name}-%{version}-src.tar.gz
Patch0: %{name}-%{version}.patch
License: GPLv2+
Group: Graphics
URL: ftp://ftp.x.org/contrib/utilities/xcolorsel-1.1a-src.tar.gz

%description
xcolorsel is a X-Utility that allows you to display X11 "rgb.txt" or
other such files together with tiles showing how the color looks on
your screen. Also a programmer may (like with xfontsel) cut the color
names/definitions in various formats (Colorformats and formats for
resourcefiles or C-sources) und paste them directly in his source
codes.

%prep
%setup -q -n xcolorsel
%patch0 -p1

%build
xmkmf -a
%{__make} XAWLIB=-lXaw3d

%install
%{__mkdir_p} $RPM_BUILD_ROOT%{_datadir}/X11/app-defaults
make install DESTDIR="$RPM_BUILD_ROOT"
rm -f $RPM_BUILD_ROOT/%{_prefix}/lib/X11/app-defaults

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc 00-ANNOUNCE 00-README 01-CHANGELOG 01-COPYING
%dir %{_prefix}/lib/X11/xcolorsel
%dir %{_datadir}/X11/app-defaults
%{_bindir}/xcolorsel
%{_datadir}/X11/app-defaults/*
%{_prefix}/lib/X11/xcolorsel/Xcolorsel.help

%changelog
* Wed Feb 01 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 1.1a
- Rebuild for Fedora
* Sun Mar 27 2011 Agnelo de la Crotche <agnelo@unixversal.com> 
- package for openSUSE 11.3/11.4 
* Sun Aug 03 2008 Thierry Vignaud <tvignaud@mandriva.com> 1.1a-4mdv2009.0
+ Revision: 262281
- rebuild
* Thu Jul 31 2008 Thierry Vignaud <tvignaud@mandriva.com> 1.1a-3mdv2009.0
+ Revision: 256677
- rebuild
* Thu Jan 03 2008 Olivier Blin <oblin@mandriva.com> 1.1a-1mdv2008.1
+ Revision: 140953
- restore BuildRoot
  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request
* Wed Aug 29 2007 Gustavo De Nardin <gustavodn@mandriva.com> 1.1a-1mdv2008.0
+ Revision: 74600
- fixed BuildRequires on Xaw3d
- 1st Mandriva xcolorsel version imported into SVN
