Name:           createtorrent
Version:        1.1.4
Release:        12.1
License:        GPL
Group:          Productivity/Networking/Other
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  openssl-devel pkgconfig
URL:            http://www.createtorrent.com/
Source:         http://www.createtorrent.com/createtorrent-%{version}.tar.gz
Summary:        A small and fast command line utility to create BitTorrent files easily

%description
CreateTorrent is a small and fast command line utility for all Linux and Unix
operating systems to create BitTorrent files easily. BitTorrent files can be
created from either one file or a collection of files that are grouped together
into a directory.

Authors:
--------
    Daniel Etzold <detzold@gmx.de>

%prep
%setup -q
sed -i 's|-lssl|-lcrypto|' configure

%build
%configure
%{__make}

%install
%{__rm} -rf $RPM_BUILD_ROOT
%makeinstall

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_bindir}/createtorrent
%doc AUTHORS ChangeLog COPYING NEWS README

%changelog
* Tue Aug 21 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 1.1.4
- Rebuilt for Fedora
* Sun Apr  8 2007 mrueckert@suse.de
- update to version 1.1.3
* Sun Mar  4 2007 mrueckert@suse.de
- update to version 1.1.2
* Fri Nov 10 2006 mrueckert@suse.de
- initial package of version 1.0.0
