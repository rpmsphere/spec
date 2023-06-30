Name:          mandvd
Epoch:         1
Version:       2.6
Release:       14.1
Summary:       A tool to generate videoDVD 
Group:         Graphical Desktop/Applications/Multimedia
URL:           https://www.kde-apps.org/content/show.php/ManDVD?content=83906
Source:        https://www.grommit.se/mandvd/mandvd-%{version}-0.fc12.tar.gz
Patch0:        mandvd-2.5-desktop.patch
License:       GPL
Requires:      dvd-slideshow
Requires:      gimp
Requires:      wodim
Requires:      xine-ui
Requires:      dvdauthor
Requires:      mjpegtools
Requires:      netpbm
Requires:      transcode
Requires:      dvd+rw-tools
Requires:      lame
BuildRequires: libpng-devel
BuildRequires: glibc-devel
BuildRequires: gcc-c++
BuildRequires: qt3-devel
BuildRequires: libstdc++-devel
BuildRequires: libX11-devel
BuildRequires: libXext-devel

%description
mandvd is a tool to generate VideoDVD.

%prep
%setup -q
%patch0 -p1
sed -i '1i #include <unistd.h>' main.cpp mandvd.cpp

%build
qmake -o Makefile mandvd.pro
sed -i 's|-Werror=format-security|-fpermissive|' Makefile
make

%install
rm -rf "$RPM_BUILD_ROOT"
install -D -m 755 %{name} $RPM_BUILD_ROOT%{_bindir}/mandvd
install -D -m 644 mandvd.desktop $RPM_BUILD_ROOT%{_datadir}/applications/mandvd.desktop
install -D -m 644 mandvdico.png $RPM_BUILD_ROOT%{_datadir}/pixmaps/mandvd.png
install -D -m 644 mandvdSplash.png $RPM_BUILD_ROOT%{_datadir}/pixmaps/mandvdSplash.png

%clean
rm -rf "$RPM_BUILD_ROOT"

%files
%doc COPYING TODO
%{_bindir}/mandvd
%{_datadir}/applications/mandvd.desktop
%{_datadir}/pixmaps/mandvd.png
%{_datadir}/pixmaps/mandvdSplash.png

%changelog
* Tue Jun 22 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 2.6
- Rebuilt for Fedora
* Thu May 13 2010 Stefano Cotta Ramusino <stefano.cotta@openmamba.org> 2.6-1mamba
- update to 2.6
- fixed spec file
* Tue Jul 22 2008 Silvan Calarco <silvan.calarco@mambasoft.it> 2.5-1mamba
- fixed version (2.5, not 4) and bumped epoch up
- added desktop file installation with italian translation
* Mon Jul 21 2008 Ercole 'ercolinux' Carpanetto <ercole69@gmail.com> 4-1mamba
- package created by autospec
