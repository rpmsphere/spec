Summary: Manfred von Thun's Programming Language Joy
Name: joy1
Version: 1.0
Release: 1
License: BSD
Group: Development/Language
URL: https://github.com/Wodan58/joy1
Source0: https://github.com/Wodan58/joy1/archive/refs/heads/master.zip#/%{name}-master.zip

%description
This is the BDW version of Joy. The two versions are drifting apart.

%prep
%setup -q -n %{name}-master

%build
cmake -DCMAKE_INSTALL_PREFIX:PATH=/usr .
make

%install
rm -rf %{buildroot}
install -Dm755 joy %{buildroot}%{_bindir}/joy

%files
%doc doc/* LICENSE README.md
%{_bindir}/joy

%changelog
* Sun Aug 8 2021 Wei-Lun Chao <bluebat@member.fsf.org> - 1.0
- Rebuilt for Fedora
