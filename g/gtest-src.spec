Summary:        Source files for gtest
Name:           gtest-src
%if %{fedora}<21
Version:        1.6.0
%else
Version:        1.7.0
%endif
Release:        5.1
License:        BSD
Group:          Development/Tools
URL:            https://code.google.com/p/googletest/
Source0:        https://googletest.googlecode.com/files/gtest-%{version}.zip
BuildArch:	noarch
Requires:	gtest-devel

%description
Source files for the package gtest.

%prep
%setup -q -n gtest-%{version}

%build

%install
rm -rf %{buildroot}
install -d %{buildroot}/usr/src/gtest
cp -r src %{buildroot}/usr/src/gtest

%files
/usr/src/gtest

%changelog
* Wed Jun 03 2015 Wei-Lun Chao <bluebat@member.fsf.org> - 1.7.0
- Rebuilt for Fedora
