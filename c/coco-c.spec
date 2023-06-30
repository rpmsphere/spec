%define _default_patch_fuzz 2

Summary:	Parser and lexer generator
Summary(pl.UTF-8):	Generator analizatorów leksykalnych i składniowych
Name:		coco-c
Version:	1.17
Release:	13.1
Group:		Development/Tools
License:	Free
Source0:	https://www.scifac.ru.ac.za/coco/cocorc17.tgz
Patch0:		CocoR-compile.patch
BuildRequires:	gcc-c++, sharutils

%description
Coco/R generator, C version.

%description -l pl.UTF-8
Generator analizatorów leksykalnych i składniowych Coco/R.

%prep
%setup -q -c
%patch0 -p1

%build
export CRFRAMES=`pwd`/frames
uudecode dos2unix.uue
chmod +x dos2unix.sh
./dos2unix.sh unix.mk
%{__make} -f unix.mk dos2unix \
	CC="gcc" \
	CXX="g++" \
	OPTFLAGS="%{optflags}"
%{__make} -f unix.mk linux \
	CC="gcc" \
	CXX="g++" \
	OPTFLAGS="%{optflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install -m755 cocor $RPM_BUILD_ROOT%{_bindir}
install -d $RPM_BUILD_ROOT%{_datadir}/coco/frames/cplus2
cp -f frames/*.frm $RPM_BUILD_ROOT%{_datadir}/coco/frames
cp -f frames/cplus2/*.frm $RPM_BUILD_ROOT%{_datadir}/coco/frames/cplus2
install -d $RPM_BUILD_ROOT%{_mandir}/man1
install docs/cocor.1 $RPM_BUILD_ROOT%{_mandir}/man1/cocor.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_bindir}/cocor
%{_mandir}/man1/cocor.1*
%{_datadir}/coco

%changelog
* Sun Dec 16 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 1.17
- Rebuilt for Fedora
* Fri Sep 14 2007 PLD Team <feedback@pld-linux.org>
All persons listed below can be reached at <cvs_login>@pld-linux.org
Revision 1.14  2007/09/14 13:25:24  baggins
- fixed version number (it was 1.15 not 1.50)
- epoch 1
- up to 1.17
Revision 1.13  2007/02/12 21:21:30  glen
- tabs in preamle
Revision 1.12  2007/02/12 00:48:33  baggins
- converted to UTF-8
Revision 1.11  2005/12/10 14:54:28  twittner
- pass to make C/C++ compilers througth CC and CXX
Revision 1.10  2005/12/09 23:22:02  baggins
- fixed compilation
Revision 1.9  2005/09/11 16:38:38  darekr
- missing dir
Revision 1.8  2004/12/15 12:17:15  radek
- minor License unifications
Revision 1.7  2003/08/06 16:47:54  kloczek
- może wrescie ktoś wykasuje to konto ?
Revision 1.6  2003/05/26 16:24:18  malekith
- massive attack: adding Source-md5
Revision 1.5  2003/05/25 05:45:21  misi3k
- massive attack s/pld.org.pl/pld-linux.org/
Revision 1.4  2002/02/22 23:28:37  kloczek
- removed all Group fields translations (oure rpm now can handle translating
  Group field using gettext).
Revision 1.3  2002/01/18 02:12:09  kloczek
perl -pi -e "s/pld-list\@pld.org.pl/feedback\@pld.org.pl/"
Revision 1.2  2001/05/02 02:43:02  qboosh
- adapterized and made spec %%debug ready or added using %%rpm*flags macros
Revision 1.1  2000/12/12 15:46:26  baggins
- initial revision
* Tue Dec 5 2000 Lukatiks <luke@agetiks.dhs.org>
- Lukatkowa sprawka (Initial version)
