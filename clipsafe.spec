Name:           clipsafe
Version:        1.1
Release:        3.1
License:        GPLv2
Group:          System/Security
Requires:       perl-Digest-SHA1 perl-Crypt-Twofish perl-DateTime
URL:            http://waxandwane.org/clipsafe.html
Source:         http://waxandwane.org/download/clipsafe-1.1.tar.gz
Summary:        A Command Line Interface to Password Safe
BuildArch:      noarch

%description
cliPSafe is a command line interface (cli) to Password Safe databases. cliPSafe
only works with version 3 databases and it currently only operates in read only
mode. Password Safe was originally written by Bruce Schneier and is now run as
an open source project hosted on SourceForge.

%prep
%setup -c

%build

%install
%{__rm} -rf $RPM_BUILD_ROOT
%{__install} -D -m 0755 clipsafe $RPM_BUILD_ROOT%{_bindir}/clipsafe

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%files
%{_bindir}/clipsafe

%changelog
* Wed Aug 01 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 1.1
- Rebuild for Fedora
* Tue Apr  5 2011 mrueckert@suse.de
- initial version (v1.1)
