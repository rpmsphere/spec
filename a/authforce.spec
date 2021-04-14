%undefine _debugsource_packages

Name:           authforce
Version:        0.9.9
Release:        18.1
Source:         authforce-0.9.9.tar.bz2
License:        GPL2
Group:          Networking/WWW
Summary:        HTTP authentication brute forcer
URL:            http://divineinvasion.net/authforce
BuildRequires:  readline-devel

%description
Authforce is an HTTP authentication brute forcer. Using various methods,
it attempts brute force username and password pairs for a site. It has 
the ability to try common username and passwords, username derivations,
and common username/password pairs. It is used to both test the security
of your site and to prove the insecurity of HTTP authentication based on
the fact that users just don't pick good passwords.

Authors:
--------------
    Panagiotis Issaris <takis@lumumba.luc.ac.be>
    henjin tai-sho <henjin@tai-sho.m4f.net>
    Juan Ezquerro <arrase@gulcas.org>

%prep
%setup -q
sed -i 's|curl/types.h|curl/curl.h|' src/http.c

%build
%ifarch aarch64
cp -f /usr/lib/rpm/config.* .
%endif
./configure --prefix=%{_prefix} --libdir=%{_libdir}
make PREFIX=%{_prefix} \
     LIBDIR=%{_libdir}

%install
%{__rm} -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/bin
mkdir -p $RPM_BUILD_ROOT/usr/share/authforce
%{__strip} src/authforce
%{__install} -m 755 src/authforce $RPM_BUILD_ROOT/usr/bin

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%files
%doc ABOUT-NLS README NEWS COPYING AUTHORS ChangeLog TODO THANKS authforcerc.sample doc/authforce.1.gz
%{_bindir}/authforce
%{_datadir}/authforce

%changelog
* Mon Feb 13 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 0.9.9
- Rebuilt for Fedora
* Thu Jun 18 2009 - Matthias Weckbecker <mweckbecker@suse.de>
- initial package with version 0.9.9
