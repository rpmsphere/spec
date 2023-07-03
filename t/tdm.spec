Name: tdm
Summary: A cdm-like session selector
Version: 0.3.2
Release: 2.1
Group: System/Utilities
License: GPLv3
URL: https://code.google.com/p/t-display-manager/
Source0: https://t-display-manager.googlecode.com/files/%{name}-%{version}.tar.xz
BuildArch: noarch

%description
A session selector written in pure bash.

%prep
%setup -q -n %{name}

%build
make PREFIX=/usr

%install
make install DESTDIR=%{buildroot} PREFIX=/usr

%files
%doc COPYING TODO
%{_bindir}/*
%{_datadir}/*

%changelog
* Mon Oct 21 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 0.3.2
- Rebuilt for Fedora
