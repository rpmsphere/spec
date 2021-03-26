%define oname	Curlew

Name:		curlew
Version:	0.2.4
Release:	7.1
Summary:	Easy to use and Free Multimedia converter
Summary(fr_FR):	Convertisseur Multimédia simple à utiliser, gratuit et open-source
License:	Waqf License
Group:		Sound/Editors and Converters
URL:		https://github.com/chamfay/Curlew
Source0:	http://sourceforge.net/projects/%{name}/files/%{name}-%{version}/%{oname}-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	intltool
BuildRequires:	python2
BuildRequires:	ghostscript-core ImageMagick
BuildRequires:	librsvg2-tools
Requires:	ffmpeg
Requires:	mencoder
Requires:	ImageMagick
Requires:	pygobject2
Requires:	xdg-utils

%description
Curlew written in python and GTK3 and it depends on (ffmpeg/avconv,
mencoder).

Main Features:
    - Easy to use with simple user interface.
    - Hide the advanced options with the ability to show them.
    - Convert to more than 100 different formats.
    - Show file information (duration, remaining time, estimated size,
    progress value).
    - Allow to skip or remove file during conversion process.
    - Preview file before conversion.
    - Convert a specified portion of file.
    - Combine subtitle with video file.
    - Show error details if exist.
    - And more ...

%description -l fr_FR
Courlis est écrit en Python et GTK3. Il s'appuie sur (ffmpeg/avconv,
mencoder).

Principales caractéristiques :
    - Facile à utiliser avec une interface pour l'utilisateur.
    - Masque les options avancées avec la possibilité de les révéler.
    - Convertit vers plus de 100 formats différents.
    - Affiche les informations du fichier (la durée, le temps restant,
    la taille estimée, la progression).
    - Permet d'abandonner la conversion ou de supprimer le fichier
    pendant le processus.
    - Prévisualisation du fichier avant la conversion.
    - Convertit une partie spécifique du fichier.
    - Combine les sous-titres avec le fichier vidéo.
    - Affiche le détail d'une éventuelle erreur.
    - Et plus encore ...

%prep
%setup -q -n %{oname}-%{version}
chmod 0644 {AUTHORS,README,LICENSE-*,ChangeLog,curlew.desktop,curlew.svg}

%build
python2 setup.py build

%install
python2 setup.py install --root=%{buildroot} --skip-build

sed -i 's|/usr/bin/python$|/usr/bin/python2|' %{buildroot}%{_bindir}/%{name}

%files
%doc ChangeLog README LICENSE* AUTHORS THANKS
%{_bindir}/%{name}*
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/*/*/*/%{name}.svg
%{_datadir}/icons/*/*/*/%{name}.png
%{python_sitelib}/%{name}-%{version}-py*.egg-info
%{_datadir}/pixmaps/%{name}.svg

%changelog
* Mon Oct 29 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 0.2.4
- Rebuild for Fedora
* Sun Jun 22 2014 daviddavid (MLO Team) <daviddavid> 0.1.22.3-1.mga4
+ new version: 0.1.22.3
* Mon Mar 17 2014 david.david (MLO Team) <david.david> 0.1.22.2-1.mga4
+ new version: 0.1.22.2
* Thu Jan 30 2014 david.david (MLO Team) <david.david> 0.1.22-0.1.mga4
+ Rebuild package for Mageia 4 (Core\MLO)
+ new version: 0.1.22
* Sat Jan 11 2014 david.david (MLO Team) <david.david> 0.1.21-0.1.mga3
+ new version: 0.1.21
* Thu Dec 12 2013 david.david (MLO Team) <david.david> 0.1.20.6-0.1.mga3
+ new version: 0.1.20.6
* Sat Oct 05 2013 david.david (MLO Team) <david.david> 0.1.20.5-0.1.mga3
+ new version: 0.1.20.5
* Tue Aug 20 2013 david.david (MLO Team) <david.david> 0.1.20.3-0.1.mga3
+ new version: 0.1.20.3
* Sat Aug 10 2013 david.david (MLO Team) <david.david> 0.1.20.1-0.1.mga3
+ new version: 0.1.20.1
* Sat Aug 03 2013 david.david (MLO Team) <david.david> 0.1.19.2-0.2.mga3
+ Revision: 0.2
- fix french translation of description
- thanks for Papoteur for his great job
* Sat Jul 27 2013 david.david (MLO Team) <david.david> 0.1.19.2-0.1.mga3
+ Revision: 0.1
- build package for Mageia 3 (Core)
- imported package curlew
