%undefine _debugsource_packages
%undefine _missing_build_ids_terminate_build

Name:		termshark
Version:	1.0.0
Release:	1
Summary:	A terminal UI for tshark
License:	MIT
Group:		Development/Other
URL:		https://termshark.io/
Source0:	%{name}-%{version}.tar.gz
#Source1:	%{name}.rpmlintrc
BuildRequires:	go >= 1.11
BuildRequires:	git-core
#BuildRequires:	upx
Requires:	tshark

%description
A terminal user-interface for tshark, inspired by Wireshark

%files
%doc README.md docs
%{_bindir}/%{name}

%prep
%setup -q

%build
GO111MODULE=on go get .
cd cmd/%{name}
go build -o %{name} %{name}.go
#upx %{name}

%install
install -d %{buildroot}%{_bindir}
install -Dm0755 cmd/%{name}/%{name} %{buildroot}%{_bindir}

%changelog
* Tue Sep 29 2020 Wei-Lun Chao <bluebat@member.fsf.org> - 1.0.0
- Rebuilt for Fedora
