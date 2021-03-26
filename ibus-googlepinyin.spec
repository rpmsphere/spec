Name:       ibus-googlepinyin
Version:    0.1.2
Release:    1
Summary:    Google pinyin for ibus
URL:        http://code.google.com/p/libgooglepinyin/
License:    APL2.0
Source0:    http://libgooglepinyin.googlecode.com/files/%{name}-%{version}.tar.bz2
Group:      User Interface/Desktops
BuildRequires:  intltool, cmake, gcc-c++
BuildArch: noarch
Requires: ibus, libgooglepinyin

%description
Google pinyin for ibus.

%prep
%setup -q -n %{name}

%build
mkdir build
pushd build
cmake ../ -DCMAKE_INSTALL_PREFIX=%{_prefix}
popd
 
make %{?_smp_mflags} -C build

%install
rm -rf %{buildroot}
make install/fast -C build DESTDIR=%{buildroot}

sed -i 's|/usr/bin/python$|/usr/bin/python2|' %{buildroot}%{_datadir}/%{name}/main.py

%clean
rm -rf %{buildroot}

%files
%{_datadir}/ibus/component/*
%{_datadir}/ibus-googlepinyin

%changelog
* Mon Mar 05 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 0.1.2
- Rebuild for Fedora
* Tue Sep  6 2011 Percy Lau <percy.lau@gmail.com> 0.1.0
- package for openSUSE
