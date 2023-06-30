Summary: Framebuffer screenshot program
Name: fbgrab
Version: 1.5
Release: 1
License: GPL
Group: Graphics
Source: https://hem.bredband.net/gmogmo/fbgrab/%{name}-%{version}.tar.xz
URL: https://hem.bredband.net/gmogmo/fbgrab/
BuildRequires: libpng-devel
BuildRequires: zlib-devel

%description 
FBGrab is a framebuffer screenshot program, capturing the linux frambuffer 
and converting it to a png-picture. FBGrab is delivered as is without any 
warranty and license is GPL version 2, see tar-ball for details.

%prep
%setup -q

%build
%make_build

%install
rm -rf $RPM_BUILD_ROOT
%make_install

%files 
%doc INSTALL
%_bindir/fbgrab
%_mandir/man1/fbgrab.1*

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Sun Oct 30 2022 Wei-Lun Chao <bluebat@member.fsf.org> - 1.5
- Rebuilt for Fedora
* Sat Jul 17 2021 tex - 1.5-1pclos2021
- new version
* Tue Jun 15 2010 Texstar <texstar at gmail.com> 1.0-3pclos2010
- update for 2010 release
