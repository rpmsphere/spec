%global debug_package %{nil}

Name:         hexer
Summary:      Vi-style Hexadecimal Binary Editor
URL:          https://gitorious.org/hexer
Group:        Editor
License:      BSD
Version:      0.2.3
Release:      4.1
Source0:      http://devel.ringlet.net/editors/hexer/hexer-%{version}.tar.gz

%description
Hexer is a Vi-style hexadecimal editor for editing binary files.

%prep
%setup -q

%build
make

%install
mkdir -p %{buildroot}%{_bindir} %{buildroot}%{_mandir}/man1
make install PREFIX=/usr MANDIR=%{_mandir}/man1 DESTDIR=%{buildroot}

%files
%doc TODO README COPYRIGHT CHANGES
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1.*

%changelog
* Mon Jan 04 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 0.2.3
- Rebuild for Fedora
