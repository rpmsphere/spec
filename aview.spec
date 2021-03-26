Summary: An ASCII art browser and animation player
Name: aview
Version: 1.3.0rc1
Release: 1.1
License: GPLv2
Group: Amusements/Graphics
Source0: http://prdownloads.sf.net/aa-project/aview-%{version}.tar.gz
URL: http://aa-project.sf.net/aview/
BuildRequires: aalib-devel

%description
Aview is a high quality ASCII art image browser (PNM file format) and the
aaflip animation player (FLI and FLC files) which is especially useful
with the Lynx browser. Aview features include the ability to save into
many formats (HTML, text, ANSI, etc.), contrast control, brightness
control, Gamma control, zoom, and three dithering modes.

%prep
%setup -q -n %{name}-1.3.0

%build
%configure
sed -i 's|-laa|-laa -lm|' Makefile
make

%install
rm -rf $RPM_BUILD_ROOT
%make_install

%clean 
rm -rf $RPM_BUILD_ROOT

%files
%doc ANNOUNCE ChangeLog AUTHORS NEWS README README.flip TODO
%{_bindir}/*
%{_mandir}/man1/*

%changelog
* Mon Mar 16 2015 Wei-Lun Chao <bluebat@member.fsf.org> - 1.3.0rc1
- Rebuild for Fedora
* Mon Jul 24 2000 Prospector <prospector@redhat.com>
- rebuilt
* Sat Jul 22 2000 Tim Powers <timp@redhat.com>
- fixed missing BuildPreReq
* Mon Jul 10 2000 Tim Powers <timp@redhat.com>
- rebuilt
* Mon Jul 03 2000 Prospector <bugzilla@redhat.com>
- automatic rebuild
* Tue May 2 2000 Tim Powers <timp@redhat.com>
- make it use percent configure instead
- patched to build for i388
* Tue May 2 2000 Tim Powers <timp@redhat.com>
- rebuilt for 7.0
* Mon Jan 3 2000 Tim Powers <timp@redhat.com>
- rebuilt for 6.2
* Tue Jul 6 1999 Tim Powers <timp@redhat.com>
- built for 6.1
* Mon Apr 26 1999 Michael Maher <mike@redhat.com>
- built package for 6.0
- added buildroot
