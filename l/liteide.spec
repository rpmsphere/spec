Name:           liteide
Version:        x36.2
Release:        1
Summary:        A simple, open source, cross-platform IDE
Group:          Development/Languages/Other
License:        MIT
URL:            https://github.com/visualfc/liteide
Source0:        https://github.com/visualfc/liteide/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  qt4-devel, qtwebkit-devel
Requires:       golang

%description
Core Features:
  * Mime type basis system
  * System environment manage
  * Build system manage
  * Debug system simple and open
  * Kate syntax and style scheme
  * WordApi complete helper

Golang Support:
  * Golang ast view
  * Godoc browser
  * Gocode helper
  * Project wizard
  * Project build
  * Source build

%prep
%setup -q -n %{name}-%{version}/liteidex
%ifarch x86_64 aarch64
sed -i 's|lib/liteide|lib64/liteide|' liteidex.pri
%endif

%build
%qmake_qt4 PREFIX=/usr
make %{?_smp_mflags}

%install
make INSTALL_ROOT=%{buildroot} install

%files
%doc LGPL_EXCEPTION.TXT LICENSE.LGPL
%{_bindir}/%{name}
%{_libdir}/%{name}
%{_includedir}/qjsonrpc

%changelog
* Thu Oct 31 2019 Wei-Lun Chao <bluebat@member.fsf.org> - x36.2
- Rebuilt for Fedora
* Tue Oct 18 2011 - saschpe@suse.de
- Initial version
