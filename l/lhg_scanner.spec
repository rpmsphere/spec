Name: lhg_scanner
Summary: Tools to access the Linux-Hardware-Guide knowledge base
Version: 0.5.2
Release: 1
Group: utils
License: Free Software
URL: https://www.linux-hardware-guide.com
Source0: %{name}-master.zip
BuildRequires: desktop-file-utils
BuildArch: noarch

%description
Open source tools to access the Linux-Hardware-Guide knowledge base, auto-detect
your hardware and find matching configuration support. Support for adding new
hardware to the data base.
This project provides a set of tools, which allow the direct access to
Linux-Hardware-Guide knowledge base (https://www.linux-hardware-guide.com).

%prep
%setup -q -n %{name}-master

%build

%install
install -d %{buildroot}%{_bindir}
install -m755 lhg-connector lhg-service scan_hardware %{buildroot}%{_bindir}

%files
%doc LICENSE README.md ToDo
%{_bindir}/lhg-connector
%{_bindir}/lhg-service
%{_bindir}/scan_hardware

%changelog
* Sun Dec 12 2021 Wei-Lun Chao <bluebat@member.fsf.org> - 0.5.2
- Rebuilt for Fedora
