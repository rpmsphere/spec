Name:          gngeo
Version:       0.8
Release:       1
Summary:       A Neogeo emulator
Group:         Graphical Desktop/Applications/Games
URL:           http://gngeo.berlios.de/?page=top_page
Source:        http://download.berlios.de/gngeo/gngeo-%{version}.tar.gz
License:       GPL
BuildRequires: SDL-devel
BuildRequires: SDL_image-devel

%description
GnGeo is a fast and powerful command line Neo Geo emulator.

%prep
%setup -q

%build
%configure
%__make

%install
rm -rf "%{buildroot}"
%makeinstall

%clean
rm -rf "%{buildroot}"

%files
%{_mandir}/man1/gngeo.1.*
%doc AUTHORS COPYING NEWS README README.GP2X TODO
%{_bindir}/gngeo
%{_datadir}/gngeo

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 0.8
- Rebuild for Fedora
* Fri Jun 20 2008 Silvan Calarco <silvan.calarco@mambasoft.it> 0.7-2mamba
- group entry fixed
* Mon Jun 09 2008 Ercole 'ercolinux' Carpanetto <ercole69@gmail.com> 0.7-1mamba
- package created by autospec
