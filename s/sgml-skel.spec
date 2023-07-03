Name:           sgml-skel
BuildRequires:  libxml2
Summary:        Helper Scripts for the SGML System
Version:        0.6
Release:        430.1
Group:          Productivity/Publishing/SGML
Requires:       libxml2
#Provides: 
License:        GPL v2 or later
# URL: 
Source0:        https://www.suse.de/~ke/%{name}/%{name}-%{version}.tar.bz2
# :pserver:anoncvs@sources.redhat.com:/cvs/docbook-tools
Source1:        docbook-tools/sgml-common/bin/install-catalog.in
Source2:        edit-xml-catalog.sh
Patch:          sgml-skel-regcat.diff
Patch1:         sgml-skel-regcat2.diff
Patch2:         sgml-skel-edit-cat.diff
BuildArch:      noarch

%description
These scripts will help prepare and maintain parts of an SGML system.


Authors:
--------
    Eric Bischoff <eric@caldera.de>
    Karl Eichwalder <ke@suse.de>

%define sgmldir %{_datadir}/sgml
%define INSTALL install -m755 -s
%define INSTALL_SCRIPT install -m755
%define INSTALL_DIR install -d -m755
%define INSTALL_DATA install -m644

%prep
%setup -q
%patch -p 1
%patch1 -p 1
# # cp -p $RPM_SOURCE_DIR/%{name}-README.SuSE .
cp %{S:1} .
cp %{S:2} .
%patch2 -p 0

%build
# CFLAGS="$RPM_OPT_FLAGS"
autoreconf -i -f
./configure --prefix=%{_prefix} --infodir=%{_infodir} \
  --datadir=%{_datadir} --mandir=%{_mandir} \
  --build $RPM_ARCH-suse-linux

%install
make install DESTDIR=$RPM_BUILD_ROOT
#{INSTALL_SCRIPT} install-catalog.in $RPM_BUILD_ROOT%{_bindir}/install-catalog
%{INSTALL_SCRIPT} edit-xml-catalog.sh \
  $RPM_BUILD_ROOT%{_bindir}/edit-xml-catalog
ln -sf sgml2xmlcat.sh $RPM_BUILD_ROOT%{_bindir}/sgmlcat2x.sh
ln -sf install-catalog $RPM_BUILD_ROOT%{_bindir}/install-catalog.sh
%{INSTALL_DIR} $RPM_BUILD_ROOT%{sgmldir}
%{INSTALL_DIR} $RPM_BUILD_ROOT%{_sysconfdir}/{sgml,xml}
%{INSTALL_DIR} $RPM_BUILD_ROOT/var/lib/sgml
touch $RPM_BUILD_ROOT%{_sysconfdir}/sgml/catalog
xmlcatalog --noout --create $RPM_BUILD_ROOT%{_sysconfdir}/xml/suse-catalog.xml
#xmlcatalog --noout --create $RPM_BUILD_ROOT%{_sysconfdir}/xml/catalog
#xmlcatalog --noout --add  "nextCatalog" "suse-catalog.xml" "suse-catalog.xml" \
#  $RPM_BUILD_ROOT%{_sysconfdir}/xml/catalog

%clean
rm -fr $RPM_BUILD_ROOT

%files
%doc AUTHORS COPYING NEWS README*
%ghost %{_sysconfdir}/sgml/catalog
%ghost %{_sysconfdir}/xml/suse-catalog.xml
#config %verify(not md5 size mtime) %{_sysconfdir}/xml/catalog
%dir %{_sysconfdir}/sgml
%dir %{_sysconfdir}/xml
%{_bindir}/*
%dir /var/lib/sgml

%changelog
* Wed Feb 01 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 0.6
- Rebuilt for Fedora
* Wed May 14 2008 ke@suse.de
- sgml-skel-edit-cat.diff: Edit catalog file in place; try to keep file
  permissions.  Reported by Jörg Mayer [bnc#386791].
* Mon May 14 2007 ke@suse.de
- PreReq /bin/mv . Reported by Andreas Jaeger [#274128].
* Mon Jan 29 2007 ke@suse.de
- Fix debug code in edit-xml-catalog.  Reported by Andreas Hanke and
  Dirk Mueller [# 237652].
* Mon Aug 14 2006 ke@suse.de
- Provide /etc/xml/catalog.
- SuSEconfig.sgml-skel: Remove it.  It was required to solve on update
  issue while introducing the /usr/share/xml hierarchy.  It is obsolete
  now.
* Wed Jan 25 2006 mls@suse.de
- converted neededforbuild to BuildRequires
* Mon Jul  4 2005 ke@suse.de
- PreReq /bin/awk; reported by Marco Michna [# 94798].
* Fri Jun 24 2005 ke@suse.de
- Add %%{_sysconfdir}/xml/suse-catalog.xml and mark it as %%ghost.
* Mon Jun 20 2005 schwab@suse.de
- Mark %%{_sysconfdir}/sgml/catalog as %%ghost and remove %%pre.
* Fri Nov 12 2004 mmj@suse.de
- cp used in %%pre so add to PreReq:
* Wed Aug 25 2004 ke@suse.de
- edit-xml-catalog.sh: Drop dependency on getopt to avoid adding more
  PreReqs in packages depending on sgml-skel.  Reported by Thorsten
  Kukuk [# 44154].
* Mon Feb 23 2004 hmacht@suse.de
- building as non-root
* Thu Feb 12 2004 ke@suse.de
- Fix tei-xsl link.
- Add svg-dtd links.
* Wed Feb 11 2004 ke@suse.de
- Correct resp. change some links; add tei-xsl-stylesheets.
* Thu Feb  5 2004 ke@suse.de
- Correct docbook-xsl-stylesheets related compat links.
- Add links for mathml-dtd.
* Fri Jan 30 2004 ke@suse.de
- Also create docbook-xsl-stylesheets related compat links (FHS 2.3
  related change).
* Fri Jan 23 2004 ke@suse.de
- Add SuSEconfig.sgml-skel: In case of an update provide compatibility
  links.
* Thu Jul 31 2003 meissner@suse.de
- autoreconf -i -f, so the --build arch switch detects ppc64.
* Fri Jun 13 2003 ke@suse.de
- Drop /usr/share/sgml from and add /etc/xml to %%files.
* Tue Apr 29 2003 ke@suse.de
- Add option --group to build <group>...</group> sections with id
  attributes in catalog files.
* Mon Apr 28 2003 ke@suse.de
- Add option --catalog to allow editing arbitrary catalog files.
* Mon Apr 28 2003 ke@suse.de
- Add edit-xml-catalog.sh, a script for editing /etc/xml/catalog.
* Wed Dec 11 2002 ke@suse.de
- sgml-skel-regcat2.diff: Don't register catalogs twice.
* Mon Nov 25 2002 ke@suse.de
- Update to version 0.6:
  * New script: sgml-register-catalog.
- sgml-skel-regcat.diff: Remove subcatalog without checking unrelated
  stuff.
* Thu Nov 21 2002 ke@suse.de
- /etc/sgml/catalog now belongs to this package; preserve backup in case
  sgmltools-lite owns it at the same time.
- Install install-catalog without suffix.
* Tue Nov 19 2002 ke@suse.de
- Add install-catalog.sh (from CVS:docbook-tools/sgml-common).
* Mon May 27 2002 ke@suse.de
- Update to version 0.5:
  - New scripts: sgml2xmlcat.sh (re-written, replacement for
    sgmlcat2x.sh) and parse-sgml-catalog.sh to normalized SGML Open
    catalogs.
* Mon May  6 2002 ke@suse.de
- Add sgmlcat2x.sh to parse normalized traditional SGML catalog files.
* Mon Aug 27 2001 ke@suse.de
- Update to version 0.2 (now it's a proper package):
  - Recognize ISO identifiers (additionally to '-//' and '+//' owner
    tags).
  - Handle language and version field.
  - More error checking.
* Thu Mar 22 2001 ke@suse.de
- New package.
