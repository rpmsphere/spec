%global debug_package %{nil}
Name:     gotop
Version:  3.0.0
Release:  1
Summary:  A terminal based graphical activity monitor inspired by gtop and vtop
License:  AGPL-3.0
Group:    System/Utility
URL:      https://github.com/cjbassi/gotop
Source0:  https://github.com/cjbassi/gotop/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires: go-rpm-macros
BuildRequires: golang

%description
Another terminal based graphical activity monitor, inspired by gtop and vtop,
this time written in Go!

%prep
%setup -q
 
%build
make dist/%{name}

%install
install -Dm755 dist/%{name} %{buildroot}%{_bindir}/%{name}

%files
%license LICENSE
%doc *.md
%_bindir/%{name}

%changelog
* Wed Dec 04 2019 Wei-Lun Chao <bluebat@member.fsf.org> - 3.0.0
- Rebuild for Fedora
