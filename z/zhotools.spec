Name:           zhotools
Version:        0.3
Release:        1
Summary:        Zhongwen Tools
License:        MPL
Group:          Applications/Utilities
Source0:        %{name}-%{version}.tar.gz
BuildArch:      noarch

%description
Using Zhongwen tables for searching, converting
and other various purposes.

%prep
%setup -q

%build
%__make

%install
%__rm -rf %{buildroot}
%__make DESTDIR=%{buildroot} install

%files
%doc README COPYING
%{_datadir}/%{name}
%{_bindir}/*

%changelog
* Wed Mar 02 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 0.1
- Initial package
