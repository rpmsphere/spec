Name: secpanel
Summary: SSH GUI for Unix
Version: 0.6.1
Release: 2.1
Group: Applications/Security
License: GPL
URL: http://www.secpanel.net
Source0: http://downloads.sourceforge.net/project/%{name}/%{name}-%{version}.tgz
BuildArch: noarch

%description
secpanel serves as graphical user interface for saving and managing
profiles for running SSH (Secure Shell) connections. It supports the
management of a ssh-agent and the generation and distribution of keys
for public key authentication. Integrates connections via SFTP using
different file browsers.

%prep
%setup -q -c

%build

%install
mkdir -p %{buildroot}
cp -a * %{buildroot}
mv %{buildroot}/usr/local/* %{buildroot}/usr
mv %{buildroot}%{_datadir}/doc/%{name}-%{version} %{buildroot}%{_datadir}/doc/%{name}

%files
%{_datadir}/doc/%{name}
%{_bindir}/*
/usr/lib/%{name}

%changelog
* Wed May 25 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 0.6.1
- Rebuild for Fedora
