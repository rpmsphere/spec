Name:				mguesser
Version:			0.4
Release:			4.1
Summary:			Text Charset and Language Guesser
# http://www.mnogosearch.org/guesser/mguesser-%{version}.tar.gz
Source:			mguesser-%{version}.tar.bz2
Patch1:			mguesser-makefile.patch
Patch2:			mguesser-fix_printf_format.patch
URL:				http://www.mnogosearch.org/guesser/
Group:			Productivity/File utilities
License:			GNU General Public License (GPL)
BuildRoot:		%{_tmppath}/build-%{name}-%{version}
BuildRequires:	make gcc glibc-devel

%description
mguesser is a standalong part of libudmsearch (a core of mnogo search engine
http://mnogosearch.org) which allows to guess text's charset and language.

Guessing is implemented using "N-Gram-Based Text Categorization" technique
which is implemented in TextCat language guesser written in Perl
(http://www.let.rug.nl/~vannoord/TextCat/). mguesser is significantly faster
than TextCat especially on large texts.

This package consist of C written N-gram based algorythms as well as a number
of maps for texts in various languages and charsets. Take a look into "maps"
directory of this package to check currently supported languages and charsets.

%prep
%setup -q
%patch1
%patch2

%build
%__make %{?jobs:-j%{jobs}} LMDIR="%{_datadir}/%{name}/maps" OPTFLAGS="%{optflags}"

%install
%__rm -rf "$RPM_BUILD_ROOT"
%__install -D -m 0755 mguesser "$RPM_BUILD_ROOT%{_bindir}/mguesser"
%__install -d "$RPM_BUILD_ROOT%{_datadir}/%{name}/maps"
%__cp maps/*.lm "$RPM_BUILD_ROOT%{_datadir}/%{name}/maps/"

%clean
%__rm -rf "$RPM_BUILD_ROOT"

%files
%defattr(-,root,root)
%doc CHANGES COPYING README
%{_bindir}/mguesser
%{_datadir}/%{name}

%changelog
* Wed Nov 30 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 0.4
- Rebuild for Fedora

* Thu Mar  6 2008 Pascal Bleser <guru@unixtech.be> 0.4
- pass optflags
- moved to openSUSE Build Service
- new upstream version

* Thu Nov 23 2006 Pascal Bleser <guru@unixtech.be> 0.2-2
- rewrote spec file, pass -j

* Mon Nov 21 2005 Pascal Bleser <guru@unixtech.be> 0.2-1
- new package
