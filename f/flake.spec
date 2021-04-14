Name:           flake
Version:        0.11
Release:        3.1
License:        LGPL-2.1+
Summary:        FLAC Audio Encoder
URL:            http://flake-enc.sourceforge.net/
Group:          Productivity/Multimedia/Sound/Utilities
Source0:        http://downloads.sourceforge.net/%{name}-enc/%{name}-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
The purpose of Flake is to be an alternative to the FLAC reference encoder
with the goal of increasing encoding speed and implementing experimental
features.

%package devel
License:        LGPL-2.1+
Summary:        Include files and libraries mandatory for development with flake
Group:          Development/Libraries/C and C++

%description devel
This package contains include files and libraries mandatory for development
with flake.

%prep
%setup -q

%build
# using %%configure gives an error so using ./configure manually
./configure \
 --prefix=%{_prefix} --libdir=%{_libdir} --incdir=%{_includedir} \
 --extra-cflags="%{optflags}" \
 --disable-strip

make

%install
%make_install

%files
%defattr(-,root,root)
%doc COPYING Changelog README
%{_bindir}/flake

%files devel
%defattr(-,root,root)
%{_includedir}/flake.h
%{_libdir}/libflake.a

%changelog
* Wed Sep 25 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 0.11
- Rebuilt for Fedora
* Sun Aug 26 2012 asterios.dramis@gmail.com
- Removed %%clean section (not needed anymore).
* Sun Oct 30 2011 asterios.dramis@gmail.com
- Initial release (version 0.11).
