Summary: Extra cin tables of OXIM
Name: oxim-tables-extra
Version: 2.0.3
Release: 1
License: Public Domain
Group: System/Internationalization
Source0: oxim-tables-extra.zip
BuildRequires: oxim
BuildArch: noarch
Requires: oxim

%description
Including extra cin tables for Open X Input Method Server.

%prep
%setup -q -n %{name}
#rm bopomofo.cin

%build
for i in *.cin ; do oxim2tab $i ; done

%install
%__rm -rf %{buildroot}
%__mkdir_p %{buildroot}%{_libdir}/oxim/tables
%__install -m 644 *.tab %{buildroot}%{_libdir}/oxim/tables

%post
oxim-agent -r

%postun
oxim-agent -r

%files
%{_libdir}/oxim/tables/*.tab

%changelog
* Sun Jul 18 2021 Wei-Lun Chao <bluebat@member.fsf.org> - 2.0.3
- Package for Fedora
