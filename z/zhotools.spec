Name:		zhotools
Version:	@VERSION@
Release:	1
Summary:	Zhongwen Tools
License:	MPL
Group:		Applications/Utilities
Source0:	%{name}-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:  sqlite
Requires:  sqlite

%description
Using Zhongwen tables for searching, converting
and other various purposes.

%prep
%setup -q

%build
make

%install
rm -rf %{buildroot}
make DESTDIR=%{buildroot} install

%clean
rm -rf %{buildroot}

%files
%doc README COPYING
%{_datadir}/%{name}
%{_bindir}/*

%changelog
* Thu Sep 03 2015 Wei-Lun Chao <bluebat@member.fsf.org> 0.5-1
- Rebuild

* Thu Jan 31 2013 Robert Wei <robert.wei@ossii.com.tw> 0.4-1.ossii
- Using sqlite3

* Wed Mar 02 2011 Wei-Lun Chao <william.chao@ossii.com.tw> 0.1-1.ossii
- Initial package
