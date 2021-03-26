%global debug_package %{nil}

Name:     sultan
Version:  18.04.01
Release:  1
Summary:  Minimarket Point Of Sales (POS) software
Group:    Office
License:  GPLv3
URL:      https://github.com/apinprastya/sultan
Source0:  %{name}-%{version}.tar.gz
BuildRequires: qt5-devel
#BuildRequires: cups-devel

%description
Minimarket POS (Point Of Sales) software writen in C++ with Qt Framework.
The main target of Sultan POS is minimarket and able to run on Raspberry Pi.

%prep
%setup -q
sed -i '1i #include <QHeaderView>' libgui/tableview.h

%build
qmake-qt5 CONFIG+=release CONFIG+=SINGLEBIN CONFIG+=NO_PRINTER_SPOOL
make %{?_smp_mflags}

%install
install -Dm755 bin/Sultan %{buildroot}%{_bindir}/%{name}

%files
%doc LICENSE README.md
%{_bindir}/%{name}

%changelog
* Thu Jan 03 2019 Wei-Lun Chao <bluebat@member.fsf.org> - 18.04.01
- Rebuild for Fedora
