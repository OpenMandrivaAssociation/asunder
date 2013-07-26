Summary:	GTK+-based audio CD ripper and encoder
Name:		asunder
Version:	2.3
Release:	1
License:	GPLv2
Group:		Archiving/Cd burning
URL:		http://littlesvr.ca/asunder/
Source0:	http://littlesvr.ca/asunder/releases/%{name}-%{version}.tar.bz2

BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(libcddb)
BuildRequires:	intltool >= 0.34.90

Requires:	cdparanoia
Suggests:	lame
Suggests:	vorbis-tools
Suggests:	flac
Suggests:	wavpack

%description
Asunder is a graphical Audio CD ripper and encoder for Linux. You can 
use it to save tracks from an Audio CD as WAV, MP3, OGG, Musepack, AAC,
Monkey Audio, and/or FLAC.

%prep
%setup -q

%build
%configure2_5x
%make

%install
%makeinstall_std

%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS ChangeLog NEWS README TODO
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png


%changelog
* Sun Feb 26 2012 Dmitry Mikhirev <dmikhirev@mandriva.org> 2.2-1
+ Revision: 780919
- update to 2.2

* Wed Jan 25 2012 Matthew Dawkins <mattydaw@mandriva.org> 2.1-1
+ Revision: 768360
- new version 2.1
- cleaned up spec
- converted BRs to pkgconfig provides

* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 1.9.1-2mdv2011.0
+ Revision: 610003
- rebuild

* Fri Dec 18 2009 Jérôme Brenier <incubusss@mandriva.org> 1.9.1-1mdv2010.1
+ Revision: 479986
- new version 1.9.1

* Wed Sep 23 2009 Emmanuel Andry <eandry@mandriva.org> 1.9-1mdv2010.0
+ Revision: 447909
- New version 1.9

* Thu Sep 10 2009 Thierry Vignaud <tv@mandriva.org> 1.6.2-2mdv2010.0
+ Revision: 436677
- rebuild

* Mon Dec 15 2008 Adam Williamson <awilliamson@mandriva.org> 1.6.2-1mdv2009.1
+ Revision: 314443
- new release 1.6.2

  + Oden Eriksson <oeriksson@mandriva.com>
    - lowercase ImageMagick

* Sat Oct 11 2008 Adam Williamson <awilliamson@mandriva.org> 1.6.1-1mdv2009.1
+ Revision: 292461
- new release 1.6.1: bugfix and translation update release only

* Wed Jul 02 2008 Adam Williamson <awilliamson@mandriva.org> 1.6-1mdv2009.0
+ Revision: 230823
- new release 1.6
- suggests wavpack (wavpack support introduced in 1.5)
- new release 1.5

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Sat Mar 01 2008 Adam Williamson <awilliamson@mandriva.org> 1.0.2-1mdv2008.1
+ Revision: 177108
- new release 1.0.2

  + Thierry Vignaud <tv@mandriva.org>
    - fix no-buildroot-tag

* Tue Dec 18 2007 Adam Williamson <awilliamson@mandriva.org> 1.0-2mdv2008.1
+ Revision: 132692
- correct summary and URL

* Tue Dec 18 2007 Adam Williamson <awilliamson@mandriva.org> 1.0-1mdv2008.1
+ Revision: 132468
- minor spec clean
- new release 1.0

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Thu Oct 11 2007 Adam Williamson <awilliamson@mandriva.org> 0.9-1mdv2008.1
+ Revision: 96958
- import asunder



