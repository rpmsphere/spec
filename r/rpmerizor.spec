Summary: Build rpm package from installed files
Summary(fr): fabrique un rpm à partie de fichiers
Name: rpmerizor
Version: 2.11
Release: 1
Group: Applications/System
License: GPL
Source: https://sourceforge.net/projects/rpmerizor/files/%{version}/%{name}-%{version}.tar.gz
URL: https://rpmerizor.sourceforge.net
BuildRequires: perl-podlators
BuildArch: noarch
Requires: perl
Requires: rpm
Requires: rpm-build

%description
Rpmerizor is a script that allows you to create an RPM package from
installed files.  You simply have to specify files on the command line
and answering a few interactive questions to fill rpm meta-data
(package name, version ...). You can also use it in batch mode with
command line options for meta-data.

%description -l fr
rpmerizor est un script perl qui permet de fabriquer un package rpm à
partir de fichier installés, en les passant en argument du programme, et en 
répondant à quelques questions interactives concernant les meta-données
(nom du package, version ...). Ces meta-données peuvent aussi être passées en
argument pour un usage batch.

%prep
%setup -q

%build
make

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install

%files
%{_bindir}/rpmerizor
%doc rpmerizor.lsm
%doc Authors
%doc COPYING
%doc Changelog
%doc Todo
%doc Makefile
%doc Readme
%{_mandir}/man1/rpmerizor.1*
%{_sysconfdir}/rpmerizorc

%changelog
* Sun Sep 25 2022 Wei-Lun Chao <bluebat@member.fsf.org> - 2.11
- Rebuilt for Fedora
* Fri Dec 2 2011 Eric Gerbier <gerbier@users.sourceforge.net> 2.6
- split dist and sign target (Makefile)
- clean target also clean signed files
- add debug option (for developpers)
- add guess option, to automatic fill all meta data
* Fri Apr 8 2011 Eric Gerbier <gerbier@users.sourceforge.net> 2.5
- in rootdir mode, guess name and version from directory name
- add compat option, for compatibility with old rpm version
- add default option, to fill release/group with default values
- guess for config/doc files from prefix
- add stdin option, to get files from stdin
* Tue Mar 22 2011 Eric Gerbier <gerbier@users.sourceforge.net> 2.4
- add url option
- add packager option
- bugfix : do not call find if no directory given
- check and create specdir/buildir if necessary
- check if rpmbuild exists
- bugfix : use mkpath instead make_path
* Thu Mar 3 2011 Eric Gerbier <gerbier@users.sourceforge.net> 2.3
- add rootdir option
- add buildarch option
- analyse rpmbuild status and fill script exit status
* Fri Feb 25 2011 Eric Gerbier <gerbier@users.sourceforge.net> 2.2
- add recursive behavior
- add list_group option
- fix rpm syntaxe on files : files containing space must be quoted
- simplify rpmbuild call
- change buildroot directory to /tmp/rpmerizor_buildroot
- change spec file prep and clean to allow work with specfile outside rpmerizor
- add comment on rpmerizor in specfile
- new man option for full help
- move pod doc in source to avoid duplicate code
- add exclude option
* Thu Feb 17 2011 Eric Gerbier <gerbier@users.sourceforge.net> 2.1
- add sign option
- save old specfile if exists
- use perl module Cwd instead external pwd call
- new option --spec_only (build spec, not package)
- add install_doc target in Makefile
- (Makefile) build man page from pod file
- rename edit option to edit_spec
- fix help on Version option
* Thu Feb 10 2011 Eric Gerbier <gerbier@users.sourceforge.net> 2.0
- make it work again with recent rpm versions
- add command line options for batch mode
- add command line option to allow build src.rpm
- add command line for editing spec file
- clean perl code
