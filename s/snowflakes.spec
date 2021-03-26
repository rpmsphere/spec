%global debug_package %{nil}

Summary: Snow flakes falling all over your desktop
Name: snowflakes
Version: 2012.1.29
Release: 6.1
URL: https://github.com/sriks/snowflakes
Source: %{name}-master.zip
License: Public Domain
Group: X11/Amusements
BuildRequires: qt4-devel

%description
It's Christmas time so it's snowflakes time. Just before this weekend I tried
snowflakes effect using Qt.

%prep
%setup -q -n %{name}-master

%build
qmake-qt4
make

%install
install -Dm755 %{name} %{buildroot}%{_bindir}/%{name}

%files
%doc readme.txt
%{_bindir}/%{name}

%changelog
* Fri Feb 23 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 2012.1.29
- Rebuild for Fedora
