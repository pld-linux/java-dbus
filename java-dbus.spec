#
# Conditional build:
%bcond_with	doc	# build full documentation
#
Summary:	Java implementation of D-BUS
Summary(pl.UTF-8):	Implementacja D-BUS w Javie
Name:		java-dbus
Version:	2.7
Release:	3
License:	AFL v2.1 or GPL v2
Group:		Libraries/Java
Source0:	http://dbus.freedesktop.org/releases/dbus-java/dbus-java-%{version}.tar.gz
# Source0-md5:	8b8470db5cd657591bac245e3b6e18e4
URL:		http://www.freedesktop.org/Software/DBusBindings
BuildRequires:	docbook-to-man
BuildRequires:	gettext-tools
BuildRequires:	java-libmatthew >= 0.6
BuildRequires:	jdk >= 1.5
BuildRequires:	jpackage-utils
BuildRequires:	rpm-javaprov
BuildRequires:	rpmbuild(macros) >= 1.300
%if %{with doc}
BuildRequires:	texlive-tex4ht
BuildRequires:	texlive-xetex
%endif
Requires:	java-libmatthew >= 0.6
Requires:	jpackage-utils
Requires:	jre >= 1.5
Obsoletes:	java-libdbus
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Java implementation of D-BUS.

%description -l pl.UTF-8
Implementacja D-BUS w Javie.

%package javadoc
Summary:	Online manual for %{name}
Summary(pl.UTF-8):	Dokumentacja online do %{name}
Group:		Documentation
Requires:	jpackage-utils

%description javadoc
Documentation for %{name}.

%description javadoc -l pl.UTF-8
Dokumentacja do %{name}.

%description javadoc -l fr.UTF-8
Javadoc pour %{name}.

%prep
%setup -q -n dbus-java-%{version}

%build
%{__make} bin man doc/api/index.html \
	PREFIX=%{_prefix} \
	JAVAUNIXLIBDIR=%{_libdir}/java
%if %{with doc}
%{__make} doc
%endif

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install-bin install-man \
	DESTDIR=$RPM_BUILD_ROOT \
	PREFIX=%{_prefix} \
	JAVAUNIXLIBDIR=%{_libdir}/java

install -d $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -a doc/api/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name} # ghost symlink

%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/libdbus-java

%clean
rm -rf $RPM_BUILD_ROOT

%post javadoc
ln -nfs %{name}-%{version} %{_javadocdir}/%{name}

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING README changelog
%if %{with doc}
%doc doc/dbus-java.pdf
%doc doc/dbus-java
%endif
%attr(755,root,root) %{_bindir}/CreateInterface
%attr(755,root,root) %{_bindir}/DBusCall
%attr(755,root,root) %{_bindir}/DBusDaemon
%attr(755,root,root) %{_bindir}/DBusViewer
%attr(755,root,root) %{_bindir}/ListDBus
%{_javadir}/dbus*.jar
%{_mandir}/man1/CreateInterface.1*
%{_mandir}/man1/DBusCall.1*
%{_mandir}/man1/DBusDaemon.1*
%{_mandir}/man1/DBusViewer.1*
%{_mandir}/man1/ListDBus.1*

%files javadoc
%defattr(644,root,root,755)
%{_javadocdir}/%{name}-%{version}
%ghost %{_javadocdir}/%{name}
