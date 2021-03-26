Name:				 unsort
Version:			 0.5
Release:			 3.1
Summary:			 Text File Line Order Randomizer
Source:			 http://www.vanheusden.com/unsort/unsort-%{version}.tgz
Patch1:         unsort-makefile.patch
URL:				 http://www.vanheusden.com/unsort/
Group:			 Productivity/Text/Utilities
License:			 GNU General Public License version 2 or later (GPL v2 or later)
BuildRoot:		 %{_tmppath}/build-%{name}-%{version}
BuildRequires:	 gcc make glibc-devel

%description
Unsort unsorts a textfile. In other words: it randomizes the order of the lines
in a file.

%prep
%setup -q
%patch1

%build
%__make %{?jobs:-j%{jobs}} \
	CFLAGS="%{optflags} -Wall -Werror" \
	VERSION="%{version}"

%install
%__rm -rf "$RPM_BUILD_ROOT"
%__make \
	DESTDIR="$RPM_BUILD_ROOT" \
	prefix="%{_prefix}" \
	mandir="%{_mandir}" \
	install

%clean
%__rm -rf "$RPM_BUILD_ROOT"

%files
%defattr(-,root,root)
%doc license.txt
%{_bindir}/unsort
%doc %{_mandir}/man1/unsort.1.*

%changelog
* Wed Nov 30 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 0.5
- Rebuild for Fedora

* Fri Jul  9 2010 pascal.bleser@opensuse.org
- initial package (0.5)
