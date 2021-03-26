Summary: Extra cin tables of OXIM
Name: oxim-tables-extra
Version: 2.0.2
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
%setup -q -c
rm bopomofo.cin

%build
for i in *.cin ; do oxim2tab $i ; done

%install
%__rm -rf %{buildroot}
%__mkdir_p %{buildroot}%{_libdir}/oxim/tables
%__install -m 644 *.tab %{buildroot}%{_libdir}/oxim/tables

%clean 
%__rm -rf %{buildroot}

%post
oxim-agent -r

%postun
oxim-agent -r

%files
%{_libdir}/oxim/tables/*.tab

%changelog
* Tue Dec 22 2015 Wei-Lun Chao <bluebat@member.fsf.org> - 2.0.2
- Package for Fedora
