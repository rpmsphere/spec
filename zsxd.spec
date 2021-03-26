Name:           zsxd
URL:            http://www.zelda-solarus.com
BuildRequires:  gcc-c++ cmake zip
Requires:       solarus
License:        GPLv3 or later
Group:          Amusements/Games/RPG
Version:        1.4
Release:        7.1
Summary:        A Zelda-like humorous game that works with Solarus
# Downloaded from http://www.zelda-solarus.com/download-zsxd_src
Source0:        %{name}-%{version}.tar.gz
BuildArch:	    noarch

%description
Zelda Mystery of Solarus XD: a humorous game that works with Solarus,
an open-source Zelda-like 2D game engine.

%prep
%setup -q

%build
cmake -DCMAKE_INSTALL_PREFIX:PATH="%{_prefix}" .
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install

%files
%doc readme.txt ChangeLog
%{_bindir}/%{name}
%{_datadir}/solarus

%changelog
* Sun May 19 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 1.4
- Rebuild for Fedora
* Thu Dec 29 2011 giacomosrv@gmail.com
- packaged zsxd version 1.4
