Summary: Non-free cin tables of OXIM
Name: oxim-tables-nonfree
Version: 2.0.1
Release: 1%{?dist}
License: Commercial
Group: System/Internationalization
Source0: oxim-tables-nonfree.zip
BuildRequires: oxim
BuildArch: noarch

%description
Including non-free cin tables for Open X Input Method Server.

%prep
%setup -q -c

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
%defattr(-,root,root)
%{_libdir}/oxim/tables/*.tab

%changelog
* Tue Jan 25 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 2.0.1-1.ossii
- Initial package
