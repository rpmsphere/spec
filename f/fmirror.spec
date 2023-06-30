Name:           fmirror
Version:        0.8.4
Release:        2.1
Summary:        Mirror directories from ftp servers

Group:          Applications/Internet
License:        GPLv2+
URL:            https://packages.debian.org/etch/fmirror
Source0:        ftp://ftp.sunet.se/pub/nir/ftp/utilities/%{name}/%{name}-%{version}.tar.gz

%description
fmirror is a C program to mirror a directory tree from a remote ftp
server. It allows regexp (regular expression) pattern matching to
help target files that are to be included and excluded. It uses a
combination of timestamp, file size and file permissions to decide
what files to transfer from the ftp server.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"
mkdir -p $RPM_BUILD_ROOT%{_defaultdocdir}/%{name}
for file in README generic.conf redhat.conf sample.conf; do
    mv $RPM_BUILD_ROOT%{_datadir}/%{name}/$file $RPM_BUILD_ROOT%{_defaultdocdir}/%{name}/$file
done
chmod -x $RPM_BUILD_ROOT%{_mandir}/man1/fmirror.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc ChangeLog COPYING README 
%{_mandir}/man*/%{name}*.*
%{_defaultdocdir}/%{name}/*.conf
%{_defaultdocdir}/%{name}/README
%{_bindir}/%{name}

%changelog
* Thu Feb 09 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 0.8.4
- Rebuilt for Fedora

* Sun Dec 28 2008 Fabian Affolter <fabian@bernewireless.net> - 0.8.4-1
- Initial package for Fedora
