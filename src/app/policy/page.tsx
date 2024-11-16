// Like a default policy and terms of service page because using Oauth requires this for google and other auth things
// will change this later because it was copied straight from auth.js website

export default function PolicyPage() {
  return (
    <div className="container mx-auto px-4 py-8">
      <section className="mb-8">
        <h2 className="text-2xl font-bold mb-4">Terms of Service</h2>
        <p className="bg-blueLight dark:bg-blueDark p-4 text-foregroundLight dark:text-foregroundDark">
          THE SOFTWARE IS PROVIDED &ldquo;AS IS&rdquo;, WITHOUT WARRANTY OF ANY KIND,
          EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
          MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
          IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
          CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
          TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
          SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
        </p>
      </section>

      <section className="mb-8">
        <h2 className="text-2xl font-bold mb-4">Privacy Policy</h2>
        <p className="bg-blueLight dark:bg-blueDark p-4 text-foregroundLight dark:text-foregroundDark mb-4">
          This site uses JSON Web Tokens and a Key-Value database for sessions
          and WebAuthn authenticators which resets every 2 hours.
        </p>
        <p className="bg-blueLight dark:bg-blueDark p-4 text-foregroundLight dark:text-foregroundDark">
          Data provided to this site is exclusively used to support signing in
          and is not passed to any third party services, other than via SMTP or
          OAuth for the purposes of authentication. And Vercel KV / Upstash for
          hosting the Key Value store. This data is deleted every 2 hours via
          cron job.
        </p>
      </section>
    </div>
  );
}