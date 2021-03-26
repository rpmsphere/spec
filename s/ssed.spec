Name:         ssed
Summary:      Super sed
Version:      3.60
Release:      6.1
URL:          http://sed.sourceforge.net/grabbag/ssed/ 
License:      GPL
Group:        System/Base
Source:       %{name}-%{version}.tar.bz2
BuildRoot:    %{_tmppath}/%{name}-%{version}-build

%description
ssed is a version of sed that supports a few new features, including Perl
regular expressions and much greater speed than GNU sed.

Authors:
--------
    Paolo Bonzini <bonzini@gnu.org>

%prep
%setup -q -n sed-%{version}

%build
%configure
%__make

%install
%__rm -rf %{buildroot}
%makeinstall

##
## rename binary to not conflict with regular sed
##
%__mv %{buildroot}%{_bindir}/sed %{buildroot}%{_bindir}/ssed

##
## rename documentation to not conflict with regular sed
##
for i in `find %{buildroot}/%{_mandir}/man1/  -type f`
do
  %__mv $i `echo $i | %__sed "s/sed\.\([0-9]\)/ssed.\1/g"`
done

for i in `find %{buildroot}/%{_infodir} -type f | grep -v "info\/dir"`
do
  %__mv $i `echo $i | %__sed "s/sed\./ssed./g"`
done

for i in `find %{buildroot}/%{_datadir}/locale/ -type f`
do
  %__mv $i `echo $i | %__sed "s/sed\.mo/ssed.mo/g"`
done

%files
%defattr(-,root,root)
%doc ABOUT-NLS AUTHORS BUGS COPYING ChangeLog NEWS README README.boot THANKS TODO
%{_bindir}/*
%{_infodir}/ssed*
%{_mandir}/man*/*
%{_datadir}/locale/*/LC_MESSAGES/*
%exclude %{_datadir}/info/dir

%changelog
* Thu Feb 28 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 3.60
- Rebuild for Fedora
* Tue Oct 8 2002 Karol Pietrzak <noodlez84@earthlink.net>
- added comments to %%install section
- made expection in %%install section for file "info"
- moved deletion of %%buildroot directory and made it smarter
* Tue Oct 8 2002 Karol Pietrzak <noodlez84@earthlink.net>
- updated Group
- added globbing to %%files man page list
* Sat Feb 16 2002 Karol Pietrzak <noodlez84@earthlink.net>
- updated group to conform to Mandrake Linux menu structure
* Tue Dec 25 2001 Karol Pietrzak <noodlez84@earthlink.net>
- initial SPEC file
