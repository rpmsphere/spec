Name: mce-devel
License: GPL
Group: Development/Libraries
Summary: Development files for mce
Version: 1.5.6
Release: 1
Source: mce-dev_1.5.6.tar.gz
BuildArch: noarch
BuildRequires: doxygen
Requires: pkgconfig

%description
This package contains headers defining the DBus method calls
provided by the Mode Control Entity, and the signals emitted by it.

%prep
%setup -q -n mce-dev-%{version}
sed -i 's|-o root -g root||' Makefile

%build
%__make

%install
%__rm -rf %{buildroot}
%__make DESTDIR=%{buildroot} install
mv %{buildroot}/usr/lib %{buildroot}%{_libdir}

%files
%{_includedir}/mce
%{_libdir}/pkgconfig/mce.pc

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 1.5.6
- Rebuilt for Fedora
