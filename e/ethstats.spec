Name:           ethstats
Version:        1.0
Release:        2.1
Summary:        Show the network device throughput

Group:          Applications/Internet
License:        Public Domain
URL:            https://freshmeat.net/projects/ethstats/
Source0:        hhttps://freshmeat.net/redir/ethstats/17872/url_tgz/%{name}-%{version}.tar.gz
BuildArch:      noarch

Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
ethstats is a script that quickly measures network device
throughput. It works by parsing the /proc/net/dev file that
the Linux kernel maintains, and thus utilizes a negligible
amount of CPU time. ethstats shows the throughput of each
device in both megabits per second and packets per second.  

%prep
%setup -q

%build

%install
rm -rf $RPM_BUILD_ROOT
install -Dp -m 0755 %{name}.pl $RPM_BUILD_ROOT%{_bindir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_bindir}/%{name}

%changelog
* Thu Feb 09 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 1.0
- Rebuilt for Fedora

* Sun Dec 28 2008 Fabian Affolter <fabian@bernewireless.net> - 1.0-1
- Initial package for Fedora
