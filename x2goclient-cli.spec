Name:           x2goclient-cli
Version:        3.0.1
Release:        2.1
Summary:        A command-line client for the x2go system

Group:          Applications/Communications
License:        GPLv2
URL:            http://www.x2go.org
Source0:        http://x2go.obviously-nice.de/deb/pool-lenny/%{name}/%{name}_%{version}-1.2.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch

Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
Requires:       perl-IO-All
Requires:       perl-Proc-Simple
Requires:       perl-Term-ReadPassword
Requires:       perl-Getopt-Long-Descriptive
Requires:       perl-Test-Strict

%description
x2goclient CLI is a commandline client which enables you to connect to a
x2go system. The client offers you the possibility to setup own clients,
programs and ideas. 

%prep
%setup -q

%build

%install
rm -rf $RPM_BUILD_ROOT
install -Dpm 0755 %{name} $RPM_BUILD_ROOT%{_bindir}/%{name}


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING LICENSE 
%{_bindir}/%{name}

%changelog
* Thu Feb 09 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 3.0.1
- Rebuild for Fedora

* Sat Nov 28 2009 Fabian Affolter <fabian@bernewireless.net> - 3.0.1-1.1.2
- Initial Package for Fedora
